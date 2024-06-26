"""BlenderCAM 'curvecamequation.py' © 2021, 2022 Alain Pelletier

Operators to create a number of geometric shapes with curves.
"""

from math import pi

from Equation import Expression
import numpy as np

import bpy
from bpy.props import (
    EnumProperty,
    FloatProperty,
    IntProperty,
    StringProperty,
)

from . import parametric


class CamSineCurve(bpy.types.Operator):
    """Object Sine """  # by Alain Pelletier april 2021
    bl_idname = "object.sine"
    bl_label = "Periodic Wave"
    bl_options = {'REGISTER', 'UNDO', 'PRESET'}

    #    zstring: StringProperty(name="Z equation", description="Equation for z=F(u,v)", default="0.05*sin(2*pi*4*t)" )
    axis: EnumProperty(
        name="Displacement Axis",
        items=(
            ('XY', 'Y to displace X axis', 'Y constant; X sine displacement'),
            ('YX', 'X to displace Y axis', 'X constant; Y sine displacement'),
            ('ZX', 'X to displace Z axis', 'X constant; Y sine displacement'),
            ('ZY', 'Y to displace Z axis', 'X constant; Y sine displacement')
        ),
        default='ZX',
    )
    wave: EnumProperty(
        name="Wave",
        items=(
            ('sine', 'Sine Wave', 'Sine Wave'),
            ('triangle', 'Triangle Wave', 'triangle wave'),
            ('cycloid', 'Cycloid', 'Sine wave rectification'),
            ('invcycloid', 'Inverse Cycloid', 'Sine wave rectification')
        ),
        default='sine',
    )
    amplitude: FloatProperty(
        name="Amplitude",
        default=.01,
        min=0,
        max=10,
        precision=4,
        unit="LENGTH",
    )
    period: FloatProperty(
        name="Period",
        default=.5,
        min=0.001,
        max=100,
        precision=4,
        unit="LENGTH",
    )
    beatperiod: FloatProperty(
        name="Beat Period Offset",
        default=0.0,
        min=0.0,
        max=100,
        precision=4,
        unit="LENGTH",
    )
    shift: FloatProperty(
        name="Phase Shift",
        default=0,
        min=-360,
        max=360,
        precision=4,
        unit="ROTATION",
    )
    offset: FloatProperty(
        name="Offset",
        default=0,
        min=-
        1.0,
        max=1,
        precision=4,
        unit="LENGTH",
    )
    iteration: IntProperty(
        name="Iteration",
        default=100,
        min=50,
        max=2000,
    )
    maxt: FloatProperty(
        name="Wave Ends at X",
        default=0.5,
        min=-3.0,
        max=3,
        precision=4,
        unit="LENGTH",
    )
    mint: FloatProperty(
        name="Wave Starts at X",
        default=0,
        min=-3.0,
        max=3,
        precision=4,
        unit="LENGTH",
    )
    wave_distance: FloatProperty(
        name="Distance Between Multiple Waves",
        default=0.0,
        min=0.0,
        max=100,
        precision=4,
        unit="LENGTH",
    )
    wave_angle_offset: FloatProperty(
        name="Angle Offset for Multiple Waves",
        default=pi/2,
        min=-200*pi,
        max=200*pi,
        precision=4,
        unit="ROTATION",
    )
    wave_amount: IntProperty(
        name="Amount of Multiple Waves",
        default=1,
        min=1,
        max=2000,
    )

    def execute(self, context):

        # z=Asin(B(x+C))+D
        if self.wave == 'sine':
            zstring = ssine(self.amplitude, self.period,
                            dc_offset=self.offset, phase_shift=self.shift)
            if self.beatperiod != 0:
                zstring += "+"+ssine(self.amplitude, self.period+self.beatperiod, dc_offset=self.offset,
                                     phase_shift=self.shift)
        elif self.wave == 'triangle':  # build triangle wave from fourier series
            zstring = str(round(self.offset, 6)) + \
                "+(" + str(triangle(80, self.period, self.amplitude))+")"
            if self.beatperiod != 0:
                zstring += '+' + \
                    str(triangle(80, self.period+self.beatperiod, self.amplitude))
        elif self.wave == 'cycloid':
            zstring = "abs("+ssine(self.amplitude, self.period,
                                   dc_offset=self.offset, phase_shift=self.shift)+")"
        elif self.wave == 'invcycloid':
            zstring = "-1*abs("+ssine(self.amplitude, self.period,
                                      dc_offset=self.offset, phase_shift=self.shift)+")"

        print(zstring)
        e = Expression(zstring, ["t"])  # make equation from string

        # build function to be passed to create parametric curve ()
        def f(t, offset: float = 0.0, angle_offset: float = 0.0):
            if self.axis == "XY":
                c = (e(t+angle_offset)+offset, t, 0)
            elif self.axis == "YX":
                c = (t, e(t+angle_offset)+offset, 0)
            elif self.axis == "ZX":
                c = (t, offset, e(t+angle_offset))
            elif self.axis == "ZY":
                c = (offset, t, e(t+angle_offset))
            return c

        for i in range(self.wave_amount):
            angle_off = self.wave_angle_offset*self.period*i/(2*pi)
            parametric.create_parametric_curve(f, offset=self.wave_distance*i, min=self.mint, max=self.maxt,
                                               use_cubic=True, iterations=self.iteration, angle_offset=angle_off)

        return {'FINISHED'}


class CamLissajousCurve(bpy.types.Operator):
    """Lissajous """  # by Alain Pelletier april 2021
    bl_idname = "object.lissajous"
    bl_label = "Lissajous Figure"
    bl_options = {'REGISTER', 'UNDO', 'PRESET'}

    amplitude_A: FloatProperty(
        name="Amplitude A",
        default=.1,
        min=0,
        max=100,
        precision=4,
        unit="LENGTH",
    )
    waveA: EnumProperty(
        name="Wave X",
        items=(
            ('sine', 'Sine Wave', 'Sine Wave'),
            ('triangle', 'Triangle Wave', 'triangle wave')
        ),
        default='sine',
    )

    amplitude_B: FloatProperty(
        name="Amplitude B",
        default=.1,
        min=0,
        max=100,
        precision=4,
        unit="LENGTH",
    )
    waveB: EnumProperty(
        name="Wave Y",
        items=(
            ('sine', 'Sine Wave', 'Sine Wave'),
            ('triangle', 'Triangle Wave', 'triangle wave')
        ),
        default='sine',
    )
    period_A: FloatProperty(
        name="Period A",
        default=1.1,
        min=0.001,
        max=100,
        precision=4,
        unit="LENGTH",
    )
    period_B: FloatProperty(
        name="Period B",
        default=1.0,
        min=0.001,
        max=100,
        precision=4,
        unit="LENGTH",
    )
    period_Z: FloatProperty(
        name="Period Z",
        default=1.0,
        min=0.001,
        max=100,
        precision=4,
        unit="LENGTH",
    )
    amplitude_Z: FloatProperty(
        name="Amplitude Z",
        default=0.0,
        min=0,
        max=100,
        precision=4,
        unit="LENGTH",
    )
    shift: FloatProperty(
        name="Phase Shift",
        default=0,
        min=-360,
        max=360,
        precision=4,
        unit="ROTATION",
    )

    iteration: IntProperty(
        name="Iteration",
        default=500,
        min=50,
        max=10000,
    )
    maxt: FloatProperty(
        name="Wave Ends at X",
        default=11,
        min=-3.0,
        max=1000000,
        precision=4,
        unit="LENGTH",
    )
    mint: FloatProperty(
        name="Wave Starts at X",
        default=0,
        min=-10.0,
        max=3,
        precision=4,
        unit="LENGTH",
    )

    def execute(self, context):
        # x=Asin(at+delta ),y=Bsin(bt)

        if self.waveA == 'sine':
            xstring = ssine(self.amplitude_A, self.period_A,
                            phase_shift=self.shift)
        elif self.waveA == 'triangle':
            xstring = str(triangle(100, self.period_A, self.amplitude_A))

        if self.waveB == 'sine':
            ystring = ssine(self.amplitude_B, self.period_B)

        elif self.waveB == 'triangle':
            ystring = str(triangle(100, self.period_B, self.amplitude_B))

        zstring = ssine(self.amplitude_Z, self.period_Z)

        print("x= " + str(xstring))
        print("y= " + str(ystring))
        x = Expression(xstring, ["t"])  # make equation from string
        y = Expression(ystring, ["t"])  # make equation from string
        z = Expression(zstring, ["t"])

        # build function to be passed to create parametric curve ()
        def f(t, offset: float = 0.0):
            c = (x(t), y(t), z(t))
            return c

        parametric.create_parametric_curve(f, offset=0.0, min=self.mint, max=self.maxt, use_cubic=True,
                                           iterations=self.iteration)

        return {'FINISHED'}


class CamHypotrochoidCurve(bpy.types.Operator):
    """Hypotrochoid """  # by Alain Pelletier april 2021
    bl_idname = "object.hypotrochoid"
    bl_label = "Spirograph Type Figure"
    bl_options = {'REGISTER', 'UNDO', 'PRESET'}

    typecurve: EnumProperty(
        name="Type of Curve",
        items=(
            ('hypo', 'Hypotrochoid', 'Inside ring'),
            ('epi', 'Epicycloid', 'Outside inner ring')
        ),
    )
    R: FloatProperty(
        name="Big Circle Radius",
        default=0.25,
        min=0.001,
        max=100,
        precision=4,
        unit="LENGTH",
    )
    r: FloatProperty(
        name="Small Circle Radius",
        default=0.18,
        min=0.0001,
        max=100,
        precision=4,
        unit="LENGTH",
    )
    d: FloatProperty(
        name="Distance from Center of Interior Circle",
        default=0.050,
        min=0,
        max=100,
        precision=4,
        unit="LENGTH",
    )
    dip: FloatProperty(
        name="Variable Depth from Center",
        default=0.00,
        min=-100,
        max=100,
        precision=4,
    )

    def execute(self, context):
        r = round(self.r, 6)
        R = round(self.R, 6)
        d = round(self.d, 6)
        Rmr = round(R - r, 6)  # R-r
        Rpr = round(R + r, 6)  # R +r
        Rpror = round(Rpr / r, 6)  # (R+r)/r
        Rmror = round(Rmr / r, 6)  # (R-r)/r
        maxangle = 2 * pi * \
            ((np.lcm(round(self.R * 1000), round(self.r * 1000)) / (R * 1000)))

        if self.typecurve == "hypo":
            xstring = str(Rmr) + "*cos(t)+" + str(d) + \
                "*cos(" + str(Rmror) + "*t)"
            ystring = str(Rmr) + "*sin(t)-" + str(d) + \
                "*sin(" + str(Rmror) + "*t)"
        else:
            xstring = str(Rpr) + "*cos(t)-" + str(d) + \
                "*cos(" + str(Rpror) + "*t)"
            ystring = str(Rpr) + "*sin(t)-" + str(d) + \
                "*sin(" + str(Rpror) + "*t)"

        zstring = '(' + str(round(self.dip, 6)) + \
            '*(sqrt(((' + xstring + ')**2)+((' + ystring + ')**2))))'

        print("x= " + str(xstring))
        print("y= " + str(ystring))
        print("z= " + str(zstring))
        print("maxangle " + str(maxangle))

        x = Expression(xstring, ["t"])  # make equation from string
        y = Expression(ystring, ["t"])  # make equation from string
        z = Expression(zstring, ["t"])  # make equation from string
        # build function to be passed to create parametric curve ()

        def f(t, offset: float = 0.0):
            c = (x(t), y(t), z(t))
            return c

        iter = int(maxangle * 10)
        if iter > 10000:  # do not calculate more than 10000 points
            print("limiting calculations to 10000 points")
            iter = 10000
        parametric.create_parametric_curve(
            f, offset=0.0, min=0, max=maxangle, use_cubic=True, iterations=iter)

        return {'FINISHED'}


class CamCustomCurve(bpy.types.Operator):
    """Object Custom Curve """  # by Alain Pelletier april 2021
    bl_idname = "object.customcurve"
    bl_label = "Custom Curve"
    bl_options = {'REGISTER', 'UNDO', 'PRESET'}

    xstring: StringProperty(
        name="X Equation",
        description="Equation x=F(t)",
        default="t",
    )
    ystring: StringProperty(
        name="Y Equation",
        description="Equation y=F(t)",
        default="0",
    )
    zstring: StringProperty(
        name="Z Equation",
        description="Equation z=F(t)",
        default="0.05*sin(2*pi*4*t)",
    )

    iteration: IntProperty(
        name="Iteration",
        default=100,
        min=50,
        max=2000,
    )
    maxt: FloatProperty(
        name="Wave Ends at X",
        default=0.5,
        min=-3.0,
        max=10,
        precision=4,
        unit="LENGTH",
    )
    mint: FloatProperty(
        name="Wave Starts at X",
        default=0,
        min=-3.0,
        max=3,
        precision=4,
        unit="LENGTH",
    )

    def execute(self, context):
        print("x= " + self.xstring)
        print("y= " + self.ystring)
        print("z= " + self.zstring)
        ex = Expression(self.xstring, ["t"])  # make equation from string
        ey = Expression(self.ystring, ["t"])  # make equation from string
        ez = Expression(self.zstring, ["t"])  # make equation from string

        # build function to be passed to create parametric curve ()
        def f(t, offset: float = 0.0):
            c = (ex(t), ey(t), ez(t))
            return c

        parametric.create_parametric_curve(f, offset=0.0, min=self.mint, max=self.maxt, use_cubic=True,
                                           iterations=self.iteration)

        return {'FINISHED'}


def triangle(i, T, A):
    s = str(A*8/(pi**2))+'*('
    for n in range(i):
        if n % 2 != 0:
            e = (n-1)/2
            a = round(((-1)**e)/(n**2), 8)
            b = round(n*pi/(T/2), 8)
            if n > 1:
                s += '+'
            s += str(a) + "*sin("+str(b)+"*t) "
    s += ')'
    return s


def ssine(A, T, dc_offset=0, phase_shift=0):
    return str(round(dc_offset, 6)) + "+" + str(round(A, 6)) + "*sin((2*pi/" + str(
        round(T, 6)) + ")*(t+" + str(round(phase_shift, 6)) + "))"

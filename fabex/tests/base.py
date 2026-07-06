from pathlib import Path
import subprocess


def build_extension(blender):
    source_dir = str(Path(__file__).parent.parent)
    output_dir = str(Path(__file__).parent.parent.parent)

    subprocess.run(
        [
            blender,
            "--background",
            "--factory-startup",
            "--command",
            "extension",
            "build",
            "--source-dir",
            source_dir,
            "--output-dir",
            output_dir,
            # "--split-platforms",
        ],
    )


def blender_command(blender, command):
    path = "test_func.py"
    Path(path).write_text(command)

    subprocess.run(
        [
            blender,
            "--background",
            "--factory-startup",
            "--python",
            path,
        ],
        shell=False,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )

    Path.unlink(path)


def activate_dependencies(self):
    import bpy

    bpy.context.preferences.system.use_online_access = True
    bpy.ops.extensions.repo_sync_all(use_active_only=False)

    dependencies = [
        "curve_tools",
        "simplify_curves_plus",
        "stl_format_legacy",
    ]

    for dependency in dependencies:
        try:
            bpy.ops.preferences.addon_enable(module=f"bl_ext.blender_org.{dependency}")
        except:
            bpy.ops.extensions.package_install(repo_index=0, pkg_id=dependency)

    addons = bpy.context.preferences.addons
    self.modules = [addon.module for addon in addons]


def get_modules(self):
    import bpy

    addons = bpy.context.preferences.addons
    self.modules = [addon.module for addon in addons]


def install_extension():
    import bpy

    version_file = Path(__file__).parent.parent / "version.py"
    with open(version_file) as f:
        lines = f.readlines()
        version = lines[0].split("(")[1].replace(",", "")
    major, minor, patch = version[0], version[1], version[2]
    path = str(Path(__file__).parent.parent.parent / f"fabex-{major}.{minor}.{patch}.zip")
    bpy.ops.extensions.package_install_files(filepath=path, repo="user_default")


def activate_engine(self):
    import bpy

    # Set the Render Engine to Fabex
    scene = bpy.context.scene
    scene.render.engine = "FABEX_RENDER"
    self.engine = scene.render.engine

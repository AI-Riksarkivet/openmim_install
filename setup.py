import platform
import subprocess

from setuptools import setup
from setuptools.command.install import install as _install


class install(_install):
    def run(self):
        _install.run(self)

        os_name = platform.system()
        if os_name == "Linux" or os_name == "macOS":
            whl_file = "mmcv-2.0.0-cp310-cp310-manylinux1_x86_64.whl"
        elif os_name == "Windows":
            whl_file = "mmcv-2.0.0-cp310-cp310-win_amd64.whl"
        else:
            raise RuntimeError(f"Unsupported OS: {os_name}")

        try:
            subprocess.check_call(["pip", "install", "-U", "torch==2.0.0"])
            subprocess.check_call(["pip", "install", whl_file])
            subprocess.check_call(["pip", "install", "mmengine==0.7.2"])
            subprocess.check_call(["pip", "install", "mmdet==3.1.0"])
            subprocess.check_call(["pip", "install", "mmocr==1.0.1"])

        except subprocess.CalledProcessError as e:
            print(f"Failed to execute custom installation commands: {e}")
            raise


setup(
    name="openmim-install",
    version="0.1.0",
    python_requires=">=3.10.0",
    install_requires=["torch==2.0.0"],
    cmdclass={
        "install": install,
    },
)

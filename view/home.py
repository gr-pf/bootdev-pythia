from rich.console import Console
from rich.panel import Panel
from rich import box
from rich.markdown import Markdown


def main():
    # console = Console(width=80)
    console = Console()
    console.rule("ellipsis")

    home_main_panel = """
# PYTHIA
## Oracle de vos données

v. 0.1.0
"""

    home_main_content = """
 Sed in metus ut sem suscipit fringilla non vel sapien. Vivamus in nunc metus. Curabitur interdum, est vitae tempus convallis, massa ex euismod nisi, quis fermentum risus tortor vel nunc. Nam quis metus et sapien accumsan sagittis. Fusce porta, lacus in porttitor rutrum, massa mauris facilisis nisi, vel tincidunt mauris nibh eget orci. Suspendisse ante justo, fermentum quis diam vitae, lacinia pellentesque urna. Etiam vehicula, magna vitae vehicula faucibus, risus mauris facilisis arcu, quis bibendum nulla mi sed sapien. Maecenas porta ipsum ac neque cursus, vitae fringilla arcu pharetra. Nam id vestibulum arcu. In hac habitasse platea dictumst.

Aenean lobortis vel sem a fringilla. Proin varius nunc risus. Aenean aliquam est at elit placerat vehicula. Nam eu augue sagittis, aliquet nunc quis, dignissim dui. Nam fringilla ut libero id imperdiet. Etiam malesuada leo cursus, pretium metus eget, vulputate velit. Proin est diam, hendrerit nec ante non, interdum euismod massa. Sed elit lorem, consectetur eget tortor non, tristique tincidunt quam. Suspendisse dolor nibh, pulvinar consequat felis eget, gravida posuere mauris. Pellentesque id gravida ipsum. In hac habitasse platea dictumst. Nulla iaculis sollicitudin quam eget eleifend. 
"""
    console.print(Panel(home_main_panel, style="color(12)", box=box.DOUBLE_EDGE))
    console.print(home_main_content)
    console.print(console.width)


if __name__ == "__main__":
    main()

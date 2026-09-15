from IPython.display import IFrame
def show_nested_eval():
    src = 'https://docs.google.com/presentation/d/1KiQWXpdcBL1LBb6IWHs1wgkraI_xtB_2_S0n5S0wx6c/embed?start=false&loop=false&delayms=60000&rm=minimal" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"'
    width = 800
    height = 450
    return IFrame(src, width, height)
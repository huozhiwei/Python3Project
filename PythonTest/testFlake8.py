from flake8.api import legacy as flake8legc

# legacy:n.遗产;遗赠财物;遗留;后遗症

styleGuide = flake8legc.get_style_guide(ignore=['F401'])
styleGuide.check_files(['demo06.py'])

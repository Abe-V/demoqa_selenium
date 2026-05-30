CHECKBOX_TREE = {
    "Home": ["Desktop", "Documents", "Downloads"],
    "Desktop": ["Notes", "Commands"],
    "Documents": ["WorkSpace", "Office"],
    "WorkSpace": ["React", "Angular", "Veu"],
    "Office": ["Public", "Private", "Classified", "General"],
    "Downloads": ["Word File.doc", "Excel File.doc"],
}

EXPANDABLE_FOLDERS = ["Home", "Desktop", "Documents", "WorkSpace", "Office", "Downloads"]

ALL_LEAVES = [
    "Notes",
    "Commands",
    "React",
    "Angular",
    "Veu",
    "Public",
    "Private",
    "Classified",
    "General",
    "Word File.doc",
    "Excel File.doc",
]

ALL_FOLDERS = list(CHECKBOX_TREE.keys())

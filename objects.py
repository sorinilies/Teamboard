from selenium.webdriver.common.by import By

class Objects:
    LIST_VIEW = "ListView"
    TREE_VIEW = "TreeView"
    WINDOW = (By.NAME, "TeamBoard")
    FILTER = (By.NAME, "Filter")
    TEAMS = (By.NAME, "Teams")
    CLOSE = (By.NAME, "Close")
    TITLE = (By.ID, "TitleBar")

    # Team
    GO_GUARDIAN = (By.NAME, "GoGuardian")
    CHROME_CLIENT = (By.NAME, "Chrome Client")

    # Track
    TRACK_GO_GUARDIAN = (By.NAME, "Chrome Client")
    TEAMBOARD = (By.NAME, "TeamBoard")
    SHOP_CONTRACTS = (By.NAME, "ShopContracts")

    # Role
    QA_AUTOMATION = (By.NAME, "QA Automation")
    QA = (By.NAME, "QA")
    DEV = (By.NAME, "Dev")
    TL = (By.NAME, "TL")

    # Availability
    DELEGATION = (By.NAME, "Delegation")
    VACATION = (By.NAME, "Vacation")
    OUT_OF_OFFICE = (By.NAME, "Out Of Office")
    BUSY = (By.NAME, "Busy")
    AVAILABLE = (By.NAME, "Available")

    # Technology
    JAVA = (By.NAME, "Java")
    NET = (By.NAME, ".Net")
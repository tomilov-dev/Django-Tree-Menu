from django.core.management.base import BaseCommand
from drawer.models import MenuModel, MenuItemModel

MAIN_MENU = "Main Menu"
SEC_MENU = "Secondary Menu"


class Command(BaseCommand):
    def crit(
        self,
        menu: MenuModel,
        name: str,
        slug: str,
        parent: MenuItemModel | None = None,
    ):
        return MenuItemModel.objects.create(
            menu=menu,
            name=name,
            slug=slug,
            parent=parent,
        )

    def create_sec_menu(self):
        menu = MenuModel.objects.create(name="Sec Menu", slug="sec_menu")

        item1 = self.crit(menu, "s1-1", "s1-1", None)
        item1_1 = self.crit(menu, "s2-1-1", "s2-1-1", item1)
        item1_2 = self.crit(menu, "s2-1-2", "s2-1-2", item1)
        item1_3 = self.crit(menu, "s2-1-3", "s2-1-3", item1)

        item2 = self.crit(menu, "s1-2", "s1-2", None)
        item2_1 = self.crit(menu, "s2-2-1", "s2-2-1", item2)
        item2_2 = self.crit(menu, "s2-2-2", "s2-2-2", item2)
        item2_3 = self.crit(menu, "s2-2-3", "s2-2-3", item2)

        item3 = self.crit(menu, "s1-3", "s1-3", None)
        item3_1 = self.crit(menu, "s2-3-1", "s2-3-1", item3)
        item3_2 = self.crit(menu, "s2-3-2", "s2-3-2", item3)
        item3_3 = self.crit(menu, "s2-3-3", "s2-3-3", item3)

    def create_main_menu(self):
        menu = MenuModel.objects.create(name="Main Menu", slug="main_menu")

        item1 = self.crit(menu, "m1-1", "m1-1", None)
        item1_1 = self.crit(menu, "m2-1-1", "m2-1-1", item1)
        item1_1_1 = self.crit(menu, "m3-1-1", "m3-1-1", item1_1)
        item1_1_1_1 = self.crit(menu, "m4-1", "m4-1", item1_1_1)
        item1_1_1_2 = self.crit(menu, "m4-2", "m4-2", item1_1_1)
        item1_1_1_3 = self.crit(menu, "m4-3", "m4-3", item1_1_1)

        item1_1_2 = self.crit(menu, "m3-1-2", "m3-1-2", item1_1)
        item1_1_3 = self.crit(menu, "m3-1-3", "m3-1-3", item1_1)

        item1_2 = self.crit(menu, "m2-1-2", "m2-1-2", item1)
        item1_2_1 = self.crit(menu, "m3-2-1", "m3-2-1", item1_2)
        item1_2_2 = self.crit(menu, "m3-2-2", "m3-2-2", item1_2)
        item1_2_3 = self.crit(menu, "m3-2-3", "m3-2-3", item1_2)

        item1_3 = self.crit(menu, "m2-1-3", "m2-1-3", item1)
        item1_3_1 = self.crit(menu, "m3-3-1", "m3-3-1", item1_2)
        item1_3_2 = self.crit(menu, "m3-3-2", "m3-3-2", item1_2)
        item1_3_3 = self.crit(menu, "m3-3-3", "m3-3-3", item1_2)

        item2 = self.crit(menu, "m1-2", "m1-2", None)
        item2_1 = self.crit(menu, "m2-2-1", "m2-2-1", item2)
        item2_2 = self.crit(menu, "m2-2-2", "m2-2-2", item2)
        item2_3 = self.crit(menu, "m2-2-3", "m2-2-3", item2)

        item3 = self.crit(menu, "m1-3", "m1-3", None)
        item3_1 = self.crit(menu, "m2-3-1", "m2-3-1", item3)
        item3_2 = self.crit(menu, "m2-3-2", "m2-3-2", item3)
        item3_3 = self.crit(menu, "m2-3-3", "m2-3-3", item3)

    def handle(self, *args, **kwargs):
        main_menu_check = MenuModel.objects.filter(name=MAIN_MENU).exists()
        sec_menu_check = MenuModel.objects.filter(name=SEC_MENU).exists()

        if not main_menu_check:
            self.create_main_menu()

        if not sec_menu_check:
            self.create_sec_menu()

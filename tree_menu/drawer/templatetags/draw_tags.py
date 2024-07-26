from django import template

from drawer.models import MenuModel, MenuItemModel


register = template.Library()


class TreeNode:
    def __init__(
        self,
        item: MenuItemModel | None = None,
        parent: "TreeNode" = None,
        children: list["TreeNode"] = None,
        opened: bool = False,
    ):
        self.item = item
        self.opened = opened

        self.parent = parent

        self.children = children
        if self.children is None:
            self.children = []


def build_tree(parent, item, slug):
    node_opened = item.slug == slug

    node = TreeNode(item=item, parent=parent, opened=node_opened)
    node.children = [build_tree(node, child, slug) for child in item.children.all()]
    node.opened = node.opened or any(child.opened for child in node.children)

    return node


@register.inclusion_tag("drawer/draw_menu.html", takes_context=True)
def draw_menu(context, menu_name: str, slug: str | None = None):
    menu = MenuModel.objects.prefetch_related("items").get(name=menu_name)
    items = menu.items.all()

    root = TreeNode()
    for item in items:
        if item.parent is None:
            root.children.append(build_tree(root, item, slug))

    return {"menu": menu, "root": root}

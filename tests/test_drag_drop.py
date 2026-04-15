from playwright.sync_api import expect, Page
import pytest #Playwright, sync_playwright, 
from pages.drag_drop_page import DragdropPage


@pytest.mark.parametrize("target", [[("B", "A"), ("A", "B"), ("B", "A")]])
def test_drag_drop(page: Page, target: list) -> None:
    """Intent: Test the drag and drop functionality on the page.
    Test dragging source elements to target element and verify the headers swap accordingly."""
    drag_drop = DragdropPage(page)
    drag_drop.open()
    
    for source_name, target_name in target:
        # 1. Get a snapshot of all current header texts
        # This returns a list like ['A', 'B']
        current_order = []
        for el in drag_drop.drag_drop_elements.all():
            current_order.append(el.locator("header").inner_text())
        
        # 2. Find the current index of the names provided in the parameters
        # No more ASCII math! Works for "A", "B", or "Apple", "Banana"
        source_idx = current_order.index(source_name)
        target_idx = current_order.index(target_name)
        
        print(f"Moving {source_name} (index {source_idx}) to {target_name} (index {target_idx})")

        # 3. Perform the drag
        drag_drop.drag_and_drop(source_name, target_name)
        
        # 4. Assert the swap
        # The physical slot where the source was should now have the target's text
        expect(drag_drop.drag_drop_elements.nth(source_idx).locator("header")).to_have_text(target_name)
        expect(drag_drop.drag_drop_elements.nth(target_idx).locator("header")).to_have_text(source_name)

@pytest.mark.parametrize("dist_from_target_edge", [0.0, 0.49, 0.60, 0.70, 1.5])
def test_drag_drop_setdist(page: Page, dist_from_target_edge: float) -> None:
    """
    Intent: Test the drag and drop functionality on the page.
    Test dragging A to B with certain distances right from B's leftmost edge and 
    verify the headers do or do not swap based on the distance dragged.
    """
    drag_drop = DragdropPage(page)
    drag_drop.open()
    drag_drop.drag_and_drop_setdist("A", "B", dist_from_target_edge)
    if (dist_from_target_edge < 0.65 or dist_from_target_edge > 1.35):
        # If we're dragging less than 50% towards the target, the swap should NOT happen
        expect(drag_drop.drag_drop_elements.first.locator("header")).to_have_text("A")
        expect(drag_drop.drag_drop_elements.nth(1).locator("header")).to_have_text("B")
    else:
        expect(drag_drop.drag_drop_elements.first.locator("header")).to_have_text("B")
        expect(drag_drop.drag_drop_elements.nth(1).locator("header")).to_have_text("A")

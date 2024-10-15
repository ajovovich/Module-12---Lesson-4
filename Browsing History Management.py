class BrowsingHistory:
    def __init__(self):
        self.history = []

    def add_page(self, page):
        self.history.append(page)
        print(f"Page '{page}' added to history.")

    def remove_page(self):
        if self.history:
            removed_page = self.history.pop()
            print(f"Page '{removed_page}' removed from history.")
            return removed_page
        else:
            print("No pages to remove.")
            return None

    def pages_viewed(self):
        return len(self.history)

    def is_empty(self):
        return len(self.history) == 0
    
browsing_history = BrowsingHistory()

# Add pages
browsing_history.add_page("Homepage")
browsing_history.add_page("About Us")
browsing_history.add_page("Contact")

# Remove a page
browsing_history.remove_page()

# Check number of pages viewed
print(f"Pages viewed: {browsing_history.pages_viewed()}")

# Check if the session is empty
print(f"Is browsing history empty? {browsing_history.is_empty()}")
# A non dynamic progress bar to provide feedback for optimization
def progress_bar(iterable: range, total: int, length=50) -> int:
    """
        Prints the progress of the program (linear - not in direct correlation to progress)
        Returns the current value of the progress

        @iterable: A start and end value to iterate through
        @total: The end value at which once met will complete
    """
    for i, item in enumerate(iterable):
        percent = i / total
        arrow = '=' * int(length * percent)
        spaces = ' ' * (length - len(arrow))
        progress_str = f"[{arrow}{spaces}] {int(percent * 100)}%"
        print(progress_str, end='\r')
        yield item


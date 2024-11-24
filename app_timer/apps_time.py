
class AppTime:
    """
    ...
    """
    def __init__(self) -> None:
        self.hours: int = 0
        self.minutes: int = 0
        self.seconds: int = 0

    def __add__(self, sec: int):
        """Adding seconds with right form"""

        seconds = self.seconds
        minutes = self.minutes
        hours = self.hours

        seconds += sec
        if seconds >= 60:
            seconds = 0
            minutes += 1
            if minutes >= 60:
                hours += 1

        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds


        return self

    def __str__(self):
        """Create formatted string of time"""
        return f"{self.hours:0>2}:{self.minutes:0>2}:{self.seconds:0>2}"

    def __repr__(self):
        """Create formatted string of time"""
        return f"{self.hours:0>2}:{self.minutes:0>2}:{self.seconds:0>2}"

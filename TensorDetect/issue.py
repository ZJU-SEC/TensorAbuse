from enum import Enum

class Issue:
    def __init__(self, severity, category, details):
        """
        Initialize an Issue object with severity level, issue category, and detailed information.
        :param severity: severity level (e.g.high, mid, low)
        :param category: issue category (e.g.Tensorabuse,lambda layer)
        :param details: detailed information
        """
        self.severity = severity
        self.category = category
        self.details = details

    def __str__(self):
        """
        Return a formatted string representation of the issue.
        """
        return f"Issue: [\nSeverity: {self.severity.value}, Category: {self.category.value}, Details: {self.details}]\n"

class Severity(Enum):
    HIGH = "high"
    MID = "mid"
    LOW = "low"
        
class Category(Enum):
    TENSOR_ABUSE = "Tensor abuse"
    LAMBDA_LAYER = "lambda layer"


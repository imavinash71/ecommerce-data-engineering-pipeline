class ETLError(Exception):
    """Base class for ETL exceptions."""
    pass


class ExtractError(ETLError):
    """Raised when extraction fails."""
    pass


class ValidationError(ETLError):
    """Raised when validation fails."""
    pass


class TransformError(ETLError):
    """Raised when transformation fails."""
    pass


class LoadError(ETLError):
    """Raised when loading fails."""
    pass
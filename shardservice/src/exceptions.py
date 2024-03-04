"""
Custom Exceptions
"""
class OptimisticVersionConflict(Exception):
    def __init__(self, message="Optimistic version conflict"):
        self.message = message
        super().__init__(self.message)
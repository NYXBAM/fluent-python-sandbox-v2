# Simple example with classes and mixins

from unittest.mock import Base


class JSONExportMixin:
    def export(self, data):
        print('Saving data in JSON format')
        

class TelegramNotifyMixin:
    def notify(self, message):
        print(f'Sending Telegram notification: {message}')
        

class BaseScanner:
    def run_scan(self):
        results = 'Scan results'
        self.export(results)



# Agregate mixins to create a new class with combined functionality
class SilentScanner(JSONExportMixin, BaseScanner):  
    """Scanner that saves results in JSON format without notifications
    """
    
class AlertScanner(JSONExportMixin, TelegramNotifyMixin, BaseScanner):
    """Scanner that saves results in JSON format and sends Telegram notifications
    """
    
    
silent_scanner = SilentScanner()
silent_scanner.run_scan()
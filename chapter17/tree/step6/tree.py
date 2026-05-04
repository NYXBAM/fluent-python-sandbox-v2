def tree(cls, level=0):
    yield cls.__name__, level
    for sub_cls in cls.__subclasses__():
        yield from tree(sub_cls, level + 1)
        
def display(cls):
    for cls_name, level in tree(cls):
        indent = ' ' * 4 * level
        print(f'{indent}{cls_name}')
        
if __name__ == '__main__':
    display(BaseException)
    
'''
BaseException
    BaseExceptionGroup
        ExceptionGroup
    Exception
        ArithmeticError
            FloatingPointError
            OverflowError
            ZeroDivisionError
        AssertionError
        AttributeError
        BufferError
        EOFError
        ImportError
            ModuleNotFoundError
            ZipImportError
        LookupError
            IndexError
            KeyError
            CodecRegistryError
        MemoryError
        NameError
            UnboundLocalError
        OSError
            BlockingIOError
            ChildProcessError
            ConnectionError
                BrokenPipeError
                ConnectionAbortedError
                ConnectionRefusedError
                ConnectionResetError
            FileExistsError
            FileNotFoundError
            InterruptedError
            IsADirectoryError
            NotADirectoryError
            PermissionError
            ProcessLookupError
            TimeoutError
            UnsupportedOperation
            itimer_error
        ReferenceError
        RuntimeError
            NotImplementedError
            PythonFinalizationError
            RecursionError
            _DeadlockError
        StopAsyncIteration
        StopIteration
        SyntaxError
            IndentationError
                TabError
            _IncompleteInputError
        SystemError
            CodecRegistryError
        TypeError
        ValueError
            UnicodeError
                UnicodeDecodeError
                UnicodeEncodeError
                UnicodeTranslateError
            NotShareableError
            UnsupportedOperation
        Warning
            BytesWarning
            DeprecationWarning
            EncodingWarning
            FutureWarning
            ImportWarning
            PendingDeprecationWarning
            ResourceWarning
            RuntimeWarning
            SyntaxWarning
            UnicodeWarning
            UserWarning
        InterpreterError
            InterpreterNotFoundError
        ExceptionGroup
        PatternError
        ArgumentError
        ArgumentTypeError
        TokenError
        _OptionError
    GeneratorExit
    KeyboardInterrupt
    SystemExit
'''
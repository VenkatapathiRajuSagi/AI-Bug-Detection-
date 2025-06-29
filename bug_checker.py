def analyze_code(code: str) -> str:
    try:
        # Simple check: Try compiling the code
        compile(code, "<string>", "exec")
        return "No syntax errors detected."
    except SyntaxError as e:
        return f"Syntax Error: {e}"
    except Exception as e:
        return f"Error: {e}"

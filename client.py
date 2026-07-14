class GeminiSparkDesktopMacroClient:
    def get_macro(self, user_instruction: str) -> dict:
        return {"macro_script": "open_app('Chrome'); select_tab(1); text_input('hello');"}
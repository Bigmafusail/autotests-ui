from ui_coverage_tool import UICoverageTracker


class _NoOpTracker:
    """Заглушка трекера, когда конфигурация ui_coverage (apps) недоступна (например в CI)."""

    def track_coverage(self, *, selector, action_type, selector_type):
        pass


try:
    # Инициализируем трекер для нашего приложения "ui-course"
    # ВАЖНО: 'ui-course' должен точно совпадать с ключом `key` в UI_COVERAGE_APPS
    tracker = UICoverageTracker(app="ui-course")
except Exception:
    # В CI или без конфига (UI_COVERAGE_APPS) используем заглушку, чтобы тесты не падали
    tracker = _NoOpTracker()
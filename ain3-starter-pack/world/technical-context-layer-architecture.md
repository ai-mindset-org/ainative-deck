---
type: leaf
namespace: technical
source: "AIN3 · практика M1 Дениса · 2026-07-14"
confidence: 0.85
asserted_by: "sonnet-5"
extracted_at: 2026-07-14
node_type: artifact
relations:
  extends: ["[[technical-context-map]]"]
  supports: ["[[technical-skill-definition]]"]
---

Денис описал многоуровневую архитектуру хранения: сырые данные (переписка в Telegram, почта, CRM) всегда остаются источником правды и никогда не удаляются, а поверх них строится нормализованный корпоративный контекстный слой, удобный для потребления агентом. Разнородные форматы (например, разные Excel от поставщиков) лучше сводить к единообразному виду детерминированным скриптом — "чем меньше мы используем агента, тем эффективнее результат".

## related
- [[technical-hub]]
- [[technical-context-map]]
- [[technical-skill-definition]]

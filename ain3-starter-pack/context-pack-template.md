# Context pack – template

```yaml
goal: "какой проверяемый результат нужен"
current: "что уже сделано и где лежит"
rules:
  - "ограничение или критерий качества"
examples:
  - "ссылка на хороший образец"
boundary:
  public: []
  team: []
  local: []
  ask_first: []
next_action: "один следующий шаг"
```

Каждое поле короткое. Raw source остаётся источником; context pack хранит рабочее состояние и ссылки.

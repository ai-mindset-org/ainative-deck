# Evidence Log – runs, claims and system changes

Evidence связывает первый результат с источником, проверкой и одной правкой harness перед следующим прогоном.

## Run receipt

```text
YYYY-MM-DD HH:MM · run · result · evidence · gap · system update · next run
```

Example:

```text
2026-07-14 16:20 · weekly digest · draft in 4m · output exists, 8/9 claims linked · one risk missing · add team chat to source map · Friday 16:00
```

## Claim ledger

| as_of | claim | source | check | result | next action |
|---|---|---|---|---|---|
| YYYY-MM-DD | что изменилось | ссылка / commit | human / automated | pass / review / fail | одна правка |

Правило: нет источника – нет факта. `review` и `fail` сохраняются как учебный сигнал.

## Run log

```text
{date time} · {run} · {result} · {evidence} · {gap} · {system update} · {next run}
```

## Review questions

1. Появился ли ожидаемый output?
2. Прошёл ли он заявленный definition of done?
3. Какой отсутствующий source, rule, example или boundary объясняет gap?
4. Какое одно изменение нужно внести в context, rule или skill до следующего run?

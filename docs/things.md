---
title: Things
template: card_grid.html
grids:
  - name: All things
    data_file: things
    show_key: true
  - name: Things with foo = bar1, hide moo
    data_file: things
    filters:
      - type: match
        key: foo
        value: bar1
    ignore_keys:
      - moo
    show_key: true
  - name: Things with foo = bar1 and role1 in roles, hide keys
    data_file: things
    filters:
      - type: match
        key: foo
        value: bar1
      - type: contains
        key: roles
        value: role1
    show_key: false
---

# Here are some things

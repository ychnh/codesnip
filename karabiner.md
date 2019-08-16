# Make sure to rebind terminal copy paste to shift control c/v

```
{
  "title": "Windows keys",
  "rules": [
    {
      "description": "swap control/command for terminal",
      "manipulators": [
        {
          "type": "basic",
          "from": {
            "key_code": "left_command"
          },
          "to": [
            {
              "key_code": "left_control"
            }
          ],
          "conditions": [
            {
              "type": "frontmost_application_if",
              "bundle_identifiers": [
                "^com\\.apple\\.Terminal"
              ]
            }
          ]
        }
      ]
    }
  ]
}
```

# Fuller example

```
{
  "title": "Windows keys",
  "rules": [
    {
      "description": "swap control/command fix home/end/redo except for iterm2/vim",
      "manipulators": [
        {
          "type": "basic",
          "from": {
            "key_code": "y",
            "modifiers": {
              "mandatory": [
                "command"
              ]
            }
          },
          "to": [
            {
              "key_code": "z",
              "modifiers": [
                "command",
                "shift"
              ]
            }
          ],
          "conditions": [
            {
              "type": "frontmost_application_unless",
              "bundle_identifiers": [
                "^org\\.vim\\.",
                "^com.googlecode.iterm2"
              ]
            }
          ]
        },
        {
          "type": "basic",
          "from": {
            "key_code": "end"
          },
          "to": [
            {
              "key_code": "e",
              "modifiers": [
                "control"
              ]
            }
          ],
          "conditions": [
            {
              "type": "frontmost_application_unless",
              "bundle_identifiers": [
                "^org\\.vim\\.",
                "^com.googlecode.iterm2"
              ]
            }
          ]
        },
        {
          "type": "basic",
          "from": {
            "key_code": "home"
          },
          "to": [
            {
              "key_code": "a",
              "modifiers": [
                "control"
              ]
            }
          ],
          "conditions": [
            {
              "type": "frontmost_application_unless",
              "bundle_identifiers": [
                "^org\\.vim\\.",
                "^com.googlecode.iterm2"
              ]
            }
          ]
        },
        {
          "type": "basic",
          "from": {
            "key_code": "left_command"
          },
          "to": [
            {
              "key_code": "left_control"
            }
          ],
          "conditions": [
            {
              "type": "frontmost_application_unless",
              "bundle_identifiers": [
                "^org\\.vim\\.",
                "^com.googlecode.iterm2"
              ]
            }
          ]
        },
        {
          "type": "basic",
          "from": {
            "key_code": "left_control"
          },
          "to": [
            {
              "key_code": "left_command"
            }
          ],
          "conditions": [
            {
              "type": "frontmost_application_unless",
              "bundle_identifiers": [
                "^org\\.vim\\.",
                "^com.googlecode.iterm2"
              ]
            }
          ]
        },
        {
          "type": "basic",
          "from": {
            "key_code": "right_command"
          },
          "to": [
            {
              "key_code": "right_control"
            }
          ],
          "conditions": [
            {
              "type": "frontmost_application_unless",
              "bundle_identifiers": [
                "^org\\.vim\\.",
                "^com.googlecode.iterm2"
              ]
            }
          ]
        },
        {
          "type": "basic",
          "from": {
            "key_code": "right_control"
          },
          "to": [
            {
              "key_code": "right_command"
            }
          ],
          "conditions": [
            {
              "type": "frontmost_application_unless",
              "bundle_identifiers": [
                "^org\\.vim\\.",
                "^com.googlecode.iterm2"
              ]
            }
          ]
        }
      ]
    }
  ]
}

```

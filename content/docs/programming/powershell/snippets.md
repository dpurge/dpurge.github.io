# Powershell snippets

## Get unix timestamp

```pwsh
[int](Get-Date -UFormat %s -Millisecond 0)
```

## Match glob pattern

```pwsh
function Test-GlobMatch {
  param (
    [string] $Value,
    [string] $pattern
  )
  
  foreach ($char in $pattern.toCharArray()) {
    $position = 0
    Switch ($char)
    {
      '?' { continue }
      '*' {
        foreach ($i in $value.Length .. $position) {
          if (Test-GlobMatch $value.Substring($i) $pattern.Substring($position + 1)) {
            return $True
          }
        }
        return $False
      }
      default {
        if ($value.Length -eq $position -or $pattern[$position] -ne $value[$position]) {
          return $False
        }
      }
    }
    $position++
  }
  return $value.Length -eq $position
}
```
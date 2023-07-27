# Powershell snippets

## Get unix timestamp

```pwsh
[int](Get-Date -UFormat %s -Millisecond 0)
```

## Match glob pattern

```pwsh
function Test-GlobMatch {
  param (
    [string] $value,
    [string] $pattern
  )
  
  $position = 0
  foreach ($char in $pattern.toCharArray()) {
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
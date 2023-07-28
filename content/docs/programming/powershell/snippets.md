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

## Remove git directories

```pwsh
Get-ChildItem -Recurse -Directory -Hidden -Include '.git' | Remove-Item -Force -Recurse
```

## Compress as standard zip

```pwsh
foreach ($item in (Get-ChildItem -Directory)) {
    7z a -mm=Deflate -mfb=258 -mpass=15 -r "${item}.zip" "${item}/*"
}
```

## Compress maximally

```pwsh
foreach ($item in (Get-ChildItem -Directory)) {
    7z a -t7z -mx=9 -mfb=273 -ms -md=31 -myx=9 -mtm=- -mmt -mmtf -md=1536m -mmf=bt3 -mmc=10000 -mpb=0 -mlc=0 "${item}.7z" "${item}"
}
```
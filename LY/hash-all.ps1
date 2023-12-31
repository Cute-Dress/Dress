Get-FileHash * -Algorithm SHA512 | Select-Object -Property @{name = 'FileName'; expression = { Split-Path $_.Path -leaf } }, @{name = 'Hash'; expression = { $_.Hash.ToLower() } } | Format-List

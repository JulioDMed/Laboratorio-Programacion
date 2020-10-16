function Ayuda-Comandos{
params{
$lista = @(Get-Command),
$keyword
}
for($i = 0; $i -lt $lista.count; $i++){
   
    if ($lista[$i] -match $keyword){
        $lista[$i] | Get-Help
  
    }
    
}
}

Ayuda-Comandos -keywords "Write"

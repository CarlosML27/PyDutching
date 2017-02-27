'''
    PyDutching v0.1

    Copyright 2017 Carlos Morente Lozano (@CarlosML27)

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
'''


try:
    linea=float(raw_input('Introduce la linea del dutching (0.75, 1.0, 1.25, ...)\n'))
except ValueError:
    print "No es un numero correcto"

decimallinea = linea % 1
if decimallinea == 0:
    lineainf = linea - 0.5
    lineasup = linea + 0.5
elif decimallinea == 0.25:
    lineainf = linea - 0.75
    lineasup = linea + 0.25
elif decimallinea == 0.75:
    lineainf = linea - 0.25
    lineasup = linea + 0.75
else:
    raise NameError('La linea del dutching no es correcta')
    
try:
    cuotainf=float(raw_input('Introduce la cuota del over {}\n'.format(lineainf)))
except ValueError:
    print "No es un numero correcto"

try:
    cuotasup=float(raw_input('Introduce la cuota del over {}\n'.format(lineasup)))
except ValueError:
    print "No es un numero correcto"

try:
    stake=float(raw_input('Introduce la cantidad de dinero que quieres apostar\n'))
except ValueError:
    print "No es un numero correcto"
    

if decimallinea == 0.0:
    stakeinf = 0.0
    while (stakeinf * cuotainf) < stake:
        stakeinf += 0.01
    stakesup = stake - stakeinf
elif decimallinea == 0.25:
    stakeinf = 0.0
    while (stakeinf * cuotainf) < (stake/2):
        stakeinf += 0.01
    stakesup = stake - stakeinf
elif decimallinea == 0.75:
    stakeinf = stake/2
    stakesup = stake/2
    diferencia = abs(((stakeinf*cuotainf)-stake) - (stakesup*cuotasup))
    nuevostakeinf = stakeinf + 0.01
    nuevostakesup = stakesup - 0.01
    nuevadiferencia = abs(((nuevostakeinf*cuotainf)-stake) - (nuevostakesup*cuotasup))
    while(nuevadiferencia < diferencia):
        stakeinf = nuevostakeinf
        stakesup = nuevostakesup
        diferencia = nuevadiferencia
        nuevostakeinf = stakeinf + 0.01
        nuevostakesup = stakesup - 0.01
        nuevadiferencia = abs(((nuevostakeinf*cuotainf)-stake) - (nuevostakesup*cuotasup))
print '{} al over {} goles (cuota {}) y {} al over {} goles (cuota {})'.format(stakeinf, lineainf, cuotainf, stakesup, lineasup, cuotasup)
raw_input()

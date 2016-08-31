# Week 2

## Active Shooter Exercise
- Two things that should not be done during an active shooter event:
  - Do not waste any seconds if you are not sure of the sounds of gunshots. React immediately.
  - Do not assume someone else is calling and wait for others to call. Take initiative and give as many information as much as possible

- Two things that should be done to do during an active shooter event:
  - Decide on to best course of action, whether to hide out or find a escape path.
  - Find the exits or even the windows which can be broken to get out and escaping should not be in the active line of shooter.

## ZeroR
- The code can be found [here] (https://github.com/amritbhanu/fss16591/tree/master/code/2/zeror.py)
- ZeroR function in ninja.rc looked like:
```
zeror() {
    python $Here/../../2/zeror.py $1 $2
}
```

- And eg11 function looked like:
```
eg11() {
    local data="data/jedit-4.1.arff"         
    local learners="j48 jrip nb rbfnet bnet zeror" 
    local goal=true                          
    
    local i="$Tmp/eg10"
    if [ -f "$i.pd" ]; then
       report pd "$i"
       report pf "$i"
    else
        crossval 5 5 "$data" $Seed $learners | grep $goal >"$i"
        gawk  '{print $2,$10}' "$i" > "$i.pd"
        gawk  '{print $2,$11}' "$i" > "$i.pf"
        eg10
   fi
}
```

- I used dataset jedit-4.1.arff file. My output:
```
pd

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,        zeror ,       0  ,     0 (*              |              ), 0.00,  0.00,  0.00,  0.00,  0.00
   2 ,           nb ,      45  ,    18 (        ---   *| --           ),25.00, 36.00, 45.00, 53.00, 60.00
   2 ,       rbfnet ,      47  ,    20 (        ------ *   ---        ),25.00, 43.00, 47.00, 60.00, 67.00
   3 ,         bnet ,      60  ,    17 (             --|-- *  -       ),40.00, 55.00, 60.00, 67.00, 71.00
   3 ,         jrip ,      60  ,    23 (          -----|   *   ---    ),33.00, 50.00, 60.00, 71.00, 80.00
   4 ,          j48 ,      72  ,    16 (               |-----  *  --  ),50.00, 65.00, 72.00, 81.00, 87.00
pf

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,        zeror ,       0  ,     0 (*              |              ), 0.00,  0.00,  0.00,  0.00,  0.00
   2 ,          j48 ,       7  ,     6 (     --   *  --|---           ), 4.00,  5.00,  7.00,  9.00, 13.00
   2 ,           nb ,       7  ,     6 (     --   *   -|-             ), 4.00,  5.00,  7.00, 10.00, 12.00
   2 ,         jrip ,       9  ,    10 (  ---        * |------        ), 2.00,  4.00,  9.00, 11.00, 15.00
   2 ,       rbfnet ,       9  ,     5 (     -----   * |----          ), 4.00,  7.00,  9.00, 11.00, 14.00
   2 ,         bnet ,      11  ,     6 (        -----  |*   ------    ), 6.00,  9.00, 11.00, 14.00, 18.00

```
- Zeror predicts no for jedit dataset whereas the target label is yes. It doesnt predict any yes labels.

## Table Reader.
- The code can be found [here] (https://github.com/amritbhanu/fss16591/tree/master/code/2/table_reader.py)
- Just run the code with **python table_reader.py**

```
outlook        mode: sunny, entropy: 1.577
temperature    mean: 73.571, std dev: 6.572
humidity       mean: 81.643, std dev: 10.285
windy          mode: FALSE, entropy: 0.985
play           mean: 1.071, std dev: 0.997
```

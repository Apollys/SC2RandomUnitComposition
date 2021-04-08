# Starcraft 2 Random Unit Composition Selector

This is currently a simple proof of concept.  The script generates a random "viable" unit composition, where *viable* is defined in the style of BeastyQT's "X to Grandmaster" challenge series.

Simply type either **t**, **p**, or **z** and receive your randomly selected unit composition:

![SC2UnitCompEx1](https://user-images.githubusercontent.com/37650759/114107400-ccdc6400-9885-11eb-94fe-28782e5093ec.gif)

Note: the numbers in brackets are just for testing purposes.  Each unit is assigned a value, where 10 means the unit could win high GM games on its own.  Then a set of units is randomly selected to have total value of between 10 and 15.

If no tier 1 units exist are selected, a limited number of additional early game units are added:

![SC2UnitCompEx2](https://user-images.githubusercontent.com/37650759/114108153-5f313780-9887-11eb-862b-512fea606214.gif)

Every output unit composition is guaranteed to be able to attack anything in the game.  For example, Oracle + Colossus would be automatically rejected as an invalid unit composition.  (I err on the side of safety in gray cases, so something like High Templar + Immortal would be rejected even though technically you could storm all air units, it's not reliable in practice.)

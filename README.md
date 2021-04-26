# Starcraft 2 Random Unit Composition Selector

This is currently a simple proof of concept.  The script generates a random "viable" unit composition, where *viable* is defined in the style of BeastyQT's "X to Grandmaster" challenge series.

Simply type either **t**, **p**, or **z** and receive your randomly selected unit composition:

![SC2UnitCompEx1](https://user-images.githubusercontent.com/37650759/114107400-ccdc6400-9885-11eb-94fe-28782e5093ec.gif)

Note: _the numbers in brackets are just for testing purposes_.  Each unit is assigned a value, where 10 means the unit could win high GM games on its own.  Then a set of units is randomly selected to have total value of between 10 and 15.

If no tier 1 units exist are selected, a limited number of additional early game units are added:

![SC2UnitCompEx2](https://user-images.githubusercontent.com/37650759/114108153-5f313780-9887-11eb-862b-512fea606214.gif)

All races now implemented:

![Ex_all](https://user-images.githubusercontent.com/37650759/116084566-cb1aea80-a652-11eb-8444-bd8155a9045f.png)

Every output unit composition is guaranteed to be able to attack anything in the game.  For example, Oracle + Colossus would be automatically rejected as an invalid unit composition.  (In grey areas, I err on the side of safety, so something like High Templar + Immortal would be rejected even though technically you could storm all air units, since it's not reliable in practice.)

---

Of course, human judgment supercedes simple algorithms, so if you get a ridiculous combination you can always reroll with just two keypresses.

---

Future refinements:
 * Weighted unit sampling - give increased probabilities of selecting spellcasters and interesting units, to avoid selections like Roach + Hydra.  Especially for zerg, this seems necessary to make interesting compositions.
 * Matchup-specific unit values - for example, Adepts are very strong in PvZ but quite weak in PvT, so a PvZ Adept could have value 6 while PvT adept has value 2-3.
 * Tune the numbers - unit values and min/max composition values were just pulled off the top of my head for a proof of concept.  T/Z are especially unrefined.

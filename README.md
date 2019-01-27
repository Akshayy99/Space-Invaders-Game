## Space Invaders game

- My attempt to re-create this iconic game in Python using pygame.

## The game has the following components:-

- Spaceship​ : The spaceship can only be moved horizontally. Move it using key ‘A’ to move
left and key ‘D’ to move it to the right.

- Aliens​ 

- Missiles​ : There are two types of missiles:

	- Type-1 : A missile is spawned each time the spacebar is clicked and is always spawned in the (row+1, column) block if the spaceship is in (row, column) when spacebar is clicked. For example, if the spaceship is in (1, 2) when spacebar is hit, the missile spawns in (2,2). The missile moves one row up every second. If a missile and alien collide, the alien gets destroyed.
	- Type-2 :  This missile is shot when the ‘S’ key is clicked, and unlike the first kind of bullet, will move two rows up every second. If this bullet collides with an alien, the alien will exist on the board for another 5 seconds. 
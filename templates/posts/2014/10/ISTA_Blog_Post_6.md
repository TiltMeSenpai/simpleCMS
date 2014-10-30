## Intro to Processing and stuffs

Right now in class, we're covering Processing, a language designed to make graphics easier. In general, Processing is simply a glorified set of libraries for Java, and does a fairly decent job of fixing all of the shortcomings of dealing with graphics (and programming in general) in Java. While it does have it's quirks, at the end of the day, it more or less accomplishes the job that it set out to do.

Processing has two "modes" that it can operate in. In it's 'static' mode, utilized either by **not** declaring the *draw* method, or throwing a call to the *noloop()* function into the body of your program, Processing will run the commands inside the body of your program once, before calling it a day. In the second 'dynamic' or 'active' mode, the *draw* method is declared, and there should be no call to the *noloop()* function. In this case, Processing will execute the contents of the *draw* method more or less as fast as it can, resulting in a smooth, animated image.

### Example Time!
```
size(400,400);

float x;
float y;

for (int i = 0; i < 20; i++) {
   x = random(360);
   y = random(360);
   ellipse(x+20, y+20, 20,20);
} 
```
<canvas data-processing-sources="{{static_url('processing/ellipses.pde')}}"></canvas>

This program, or "sketch," as processing calls them, generates 20 circles in random positions on the canvas. Each call to random() generates a random number between 0 and the first parameter (360 in this case). The call to ellipse() draws an ellipse on the canvas, centered around the coodinates of the first and second parameters, and with height and width of the third and fourth parameters (All respectively).

So what else can we make this program do? For one, we can always add more shapes. By telling the for loop to run through more iterations, more shapes get drawn on the screen.
```
size(400,400);

float x;
float y;

for (int i = 0; i < 100; i++) {
   x = random(360);
   y = random(360);
   ellipse(x+20, y+20, 20,20);
} 
```

Now instead of 'i < 20', we have 'i < 100' for the ending parameter. This means that the contents of the loop (Drawing an ellipse on a random position to the canvas) will be run 100 times instead of 20.

<canvas data-processing-sources="{{static_url('processing/moarEllipses.pde')}}"></canvas>

If we want different colors, we can use the 'fill' call, which will set the fill color for the next shape we draw.
```
size(400,400);

float x;
float y;

for (int i = 0; i < 100; i++) {
   x = random(360);
   y = random(360);
   fill(random(255), random(255), random(255))
   ellipse(x+20, y+20, 20,20);
} 
```

Now, right before drawing an ellipse, the fill color of the next shape is set to a random color. Easy enough, now our sketch has pretty colors.

<canvas data-processing-sources="{{static_url('processing/moarColorsAndEllipses.pde')}}"></canvas>

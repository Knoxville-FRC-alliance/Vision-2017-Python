# Vision processing for the 2018 FIRST Power Up Game
This is a collaborative project between Knoxville area FRC teams to create a platform teams can use to find the 2018 vision targets. Because every team has different code bases and movement schemes, we only report the bearing and distance to the selected target. What is done with this information is up to the individual teams. 
## Terms
**Bearing**
> The bearing is the angle from straight ahead of the camera's field of view to the target. Positive angles indicate that the target is to the right of center. Negative values indicate the target is to the left of center. Bearings should be reported in degrees as these are easier for humans to debug but a flag to report in radians may be added later because machines love radians.

 **Distance**
> Distance is reported as the linear distance along the ground from a point directly underneath the camera and sitting on the carpet to the point directly underneath the center of the selected target. It is derived from robot specific information such as where the camera is mounted, and the slant range.

## Platform
The code base is built to run on the Raspberry Pi 3 but hopefully because it is Python, it can easily run on the side processor of your choice. The Raspberry Pi was chosen because it's cheap at ~$35 and many teams already have them. Other good choices include Banana Pi, Orange Pi, Kangaroo (x86, and integrated battery), or even a Jetson TK1 (most expensive and power hungry but gives the most processing power). Python was chosen over C++ because it's beginner friendly, cross platform, and not significantly operationally slower than C++ since all the heavy processing is still done in C++ via OpenCV hooks. Additionally python has some of the fastest debugging tools so development time is accelerated here. Any other math done on arrays should be done with NumPy to keep things fast. We use Python 3 because Python 2 meets end of life in 2020 and we are thinking ahead. OpenCV v3.4 is the version of choice as it is the latest and greatest as of Jan '18. 
## Contributing
Help is always appreciated. If you find an issue open an issue and describe how best we can replicate the issue. Comment your code liberally. Example the purpose of functions with a comment block at the top. To submit changes, make a pull request. If you make a few pull requests that are approved, we will likely add you to the organization so you can have direct write access to accelerate things. It is best to work in your own branch though until individual features are stabilized and then merge the changes into the 'master' branch. [PEP8](https://www.python.org/dev/peps/pep-0008/) compliance should be strived for but don't worry about it initially. Get working code first, then clean it up so other people can read it. Having it helps other people (and yourself in a few months) read your code and understand what's going on but doesn't change performance. Don't bother trying to remember all the rules to it: download a linter and turn it on with pep8 rules when you want to clean up your code.
##### Git Commit Messages
* Use the present tense ("Add feature" not "Added feature")
* Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
* Limit the first line to 72 characters or less
* Reference issues and pull requests liberally
* [Gitmoji](https://gitmoji.carloscuesta.me/) is encouraged but not required in commit messages. It improves message function readability at a glance.
	* Consider starting the commit message with an applicable emoji:
	    * ✨ `:sparkles:` when adding a new feature
	    * 🔥 `:fire:` when removing code or files
	    * 🐛 `:bug:` when fixing a bug
	    * 🎨 `:art:` when improving the format/structure of the code
	    * ⚡️ `:zap:` when improving performance / FPS
	    * 📝 `:memo:` when writing docs
	    * 💄 `:lipstick:` when working on UI/camera overlay stuff
	    * ✅ `:white_check_mark:` when adding tests
	    * 🚧 `:construction:` work in progress commit just to save status
	    * 💥 `:boom:` Commit breaks things -- not pushed until followed with one that fixes things
	    * ♻️ `:recycle:` when refactoring code
	    * 🚨 `:rotating_light:` when removing linter warnings / moving towards [PEP8](https://www.python.org/dev/peps/pep-0008/) compliance 
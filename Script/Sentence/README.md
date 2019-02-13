## The Sentence
Version 0.2

### The "Sentence" script makes:
>1. Defines new words in a sentence.
>2. Identifies all new offers
>3. Determines the uniqueness of the offer.

### The "Sentence" script does not allow:

>1. Symbols such as "0-9.,!? <> @ # $% And others.
>2. Duplicate words in a sentence.
>3. The usual rearrangement of words in the sentence.

#### What is a Problem?

Sentence is `'dog is in ocean'`, so: <br>
These sentences are correct:
> dog is in `canoe` <br>
> `god` is in ocean
> ...

And these sentences are incorrect:
> dog !`in is` ocean <br>
> other permutations of original sentence

#### Some Example
> [Dog is god]:
![alt text](https://github.com/dpaniq/Python/blob/master/Script/Sentence/img/Dog%20is%20god.png)

> [Dog is in ocean]:
![alt text][Dog is in ocean](https://github.com/dpaniq/Python/blob/master/Script/Sentence/img/Dog%20is%20in%20ocean.png)

> [Like this]:
![alt text][Like this](https://github.com/dpaniq/Python/blob/master/Script/Sentence/img/Like%20this.png)

> [Real swords]:
![alt text](https://github.com/dpaniq/Python/blob/master/Script/Sentence/img/Real%20swords.png)

> [Miss roses act]:
![alt text](https://github.com/dpaniq/Python/blob/master/Script/Sentence/img/Miss%20roses%20act.png)


#### Idea how do better:

##### Letters in word:

If word > 8 letter, then need to rearrange 1/2 of word permutation, and leave other

##### Words in sentence:
Leave only one variable of sentence permutation possible.

For example:

god is ocean --> `is god canoe` --> *(Stop! other like - `is canoe god` or `god canoe is` dropped)*


#### Problem

>[Problem]:
![alt text](https://github.com/dpaniq/Python/blob/master/Script/Sentence/img/Problem.png)

The number of letters and words more than 8 is allowed, but the time of the permutation grows exponentially and after 8 words 30 seconds +.

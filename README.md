# SFSymbolsSafe

The new [SF Symbols](https://developer.apple.com/design/human-interface-guidelines/sf-symbols/overview/) Apple has provided are an excellent set of a lot of sweet icons to use in iOS apps.

However, if you're like me, raw string APIs like this scare the living daylights out of you:

```swift
Image(systemName: "bubble.left.and.bubble.right.fill")
```

Toss in a quick typo into that string and you've got yourself a runtime crash. You'd better hope you have a test case that covers this.

I wanted a better way to do this. So I made one. Now you can use it too.

```swift
Image(symbol: .bubbleLeftAndBubbleRightFill)
```

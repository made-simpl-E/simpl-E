# simpl-E
Simpl-E (pronounced as either 'simple E' or 'simply') is a programming language with the pure purpose of being designed for beginners who want to learn the basics of programming.

The language currently exists as only an idea(and an incredibly basic implementation), so anyone wanting to learn a programming language should look elsewhere for now.

## Current Status
Simpl-E is in a **very** early state, currently it should not be used by anyone as it doesn't do much right now.

Here is what currently works:
  1. Lexer <br>
    - most initial tokens implemented
  2. Parser <br>
    - only basic grammer rules implemented
    - no AST yet
  3. Symbol Table <br>
    - not yet implemented
  4. Testing
    - actual tests are not yet constructed
    
## How Programs will be Run
Simpl-E programs will be parsed into an Abstract Syntax Tree and then translated into the resulting python program. Python will be used, as it is a dynamic interpreted language, so simpl-E will also be dynamic and interpreted. Python also has an extensive standard library that simpl-E can use from. 

Simpl-E's grammer rules and tokens will be designed to be as easily understood as possible (especially for people who have never wrote a program before). The install process, while not yet designed, should be as simple as possible for people to install the language and write a program.

These aspects should hopefully allow simpl-E to become a great language for new learners who want to learn how to program in a very simple language before moving on to other major programming languages such as python. The main goal of this language is and will always be to open the door to programming to as many people as possible.

## Future Plans

1. Add all grammer rules to parser
1. Create symbol table
1. Construct AST
1. Write tests
1. Decide how to run programs

### Contributing

I'm not currently looking for any official contributors, but I will be once a program can be run in the language. 

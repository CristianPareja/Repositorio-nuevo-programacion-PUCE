texto="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer et nunc in ligula finibus lobortis. Curabitur dignissim libero neque. Vivamus felis risus, interdum at commodo eget, consectetur eu mi. Etiam euismod porttitor erat quis tristique. Cras tincidunt interdum metus, quis cursus ligula lobortis a. Maecenas ac nulla ut eros ullamcorper pharetra. Duis feugiat, augue mattis scelerisque placerat, risus nunc congue purus, eu porttitor dolor tellus eget magna.

Aenean varius libero sit amet lorem auctor volutpat. Cras euismod congue leo, nec mollis arcu ultricies id. Curabitur ornare nulla eleifend iaculis bibendum. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Aliquam nec eros sit amet risus laoreet ultricies sed ac odio. In faucibus commodo congue. Nullam eu bibendum augue. Nulla sagittis diam a mauris scelerisque sodales. Sed finibus vehicula mauris, vitae vulputate diam ultricies vitae. Vivamus lacus ex, tincidunt nec laoreet vel, lacinia vitae ex"""

contador=0
caracter=(input("ingrese el caracter que desee contabilizar: "))

for letra in texto:
    if letra == caracter:
        contador+=1
print(contador)

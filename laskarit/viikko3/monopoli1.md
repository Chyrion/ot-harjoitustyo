# Monopolin luokkakaavio

```mermaid
classDiagram
  Pelaaja "2..8" -- Pelilauta
  Pelinappula "1" --> Pelaaja
  Ruutu "40" --|> Pelilauta
  Ruutu --> Ruutu
  Pelinappula "1" ..> Ruutu
```

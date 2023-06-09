% ФИО: Акондзо Жордани Лади Гаэл
% Группа : НКНбд-01-21
% Вариант 9

% комплектующее: (id, название, тип, марка, дата производства)

composant(cpu, 'Intel Core i7-10700K', processeur, intel, '2020-05-27').
composant(gpu, 'NVIDIA GeForce RTX 3080', carte_graphique, nvidia, '2020-09-17').
composant(mobo, 'ASUS ROG MAXIMUS XIII HERO', carte_mere, asus, '2021-02-15').
composant(ram, 'Corsair Vengeance RGB Pro 32GB', memoire_vive, corsair, '2020-10-01').
composant(storage, 'Samsung 970 EVO Plus 1TB', disque_dur, samsung, '2019-12-11').
composant(psu, 'Corsair RM850x', alimentation, corsair, '2018-09-04').

%интерфейс подключения: (комплектующее, интерфейс)

interface(cpu, lga1200).
interface(gpu, pcie4).
interface(mobo, lga1200).
interface(mobo, pcie4).
interface(mobo, ddr4).
interface(ram, ddr4).
interface(storage, m2).

%слоты: (комплектующее, слот для подключения другого оборудования)

slots(mobo, pcie4_x16_1).
slots(mobo, pcie4_x16_2).
slots(mobo, pcie4_x8_1).
slots(mobo, pcie4_x4_1).
slots(mobo, m2_1).
slots(mobo, m2_2).

%продукт: (комплектующее, цена)

produit(cpu, 369.99).
produit(gpu, 699.99).
produit(mobo, 599.99).
produit(ram, 184.99).
produit(storage, 179.99).
produit(psu, 139.99).

% Правило

compatible(X, Y) :-
    interface(X, IF),
    interface(Y, IF).

assemblage_possible(Composants) :-
    length(Composants, N),
    N >= 5,
    N =< 7,
    member(cpu, Composants),
    member(gpu, Composants),
    member(mobo, Composants),
    member(ram, Composants),
    member(storage, Composants),
    member(psu, Composants),
    compatible(cpu, mobo),
    compatible(gpu, mobo),
    compatible(ram, mobo),
    compatible(storage, mobo),
    compatible(psu, mobo),
    findall(P, (member(C, Composants), produit(C, P)), Prix),
    sum_list(Prix, Total),
    write('Coût total du PC fini: $'),
    write(Total).

composants_disponibles(Type) :-
    findall(N, composant(_, N, Type, _, _), Noms),
    write('Composants disponibles de type '),
    write(Type),
    write(': '),
    write(Noms).

# app.py
# -*- coding: utf-8 -*-
"""
Streamlit 원소주기율표 웹앱
- 118개 원소를 주기율표 레이아웃(18열)로 표시
- 각 원소를 클릭하면 5가지 정보 표시: [실생활 사례, 원소 이름, 원소번호, 원소 특징, 미래 활용 방향]
- 좌측 검색/필터: 심볼, 이름, 그룹, 주기, 계열(알카리/할로겐/전이금속 등)
- 데이터는 코드 내에 내장(오프라인 동작). 필요 시 CSV로 내보내거나 수정 가능.


실행방법
$ streamlit run app.py
"""


import streamlit as st
from dataclasses import dataclass
from typing import Dict, List, Optional


# ------------------------- 기본 데이터 -------------------------
@dataclass
class Element:
Z: int
symbol: str
name: str
period: int
group: int


# Z순서 기본 목록 (심볼과 영문명)
# — 간결성을 위해 이름은 영어 표기 사용. 필요하면 한국어 이름으로 바꿔도 됨.
ELEMENTS_ORDERED: List[Element] = [
Element(1, "H", "Hydrogen", 1, 1),
Element(2, "He", "Helium", 1, 18),
Element(3, "Li", "Lithium", 2, 1),
Element(4, "Be", "Beryllium", 2, 2),
Element(5, "B", "Boron", 2, 13),
Element(6, "C", "Carbon", 2, 14),
Element(7, "N", "Nitrogen", 2, 15),
Element(8, "O", "Oxygen", 2, 16),
Element(9, "F", "Fluorine", 2, 17),
Element(10, "Ne", "Neon", 2, 18),
Element(11, "Na", "Sodium", 3, 1),
Element(12, "Mg", "Magnesium", 3, 2),
Element(13, "Al", "Aluminium", 3, 13),
Element(14, "Si", "Silicon", 3, 14),
Element(15, "P", "Phosphorus", 3, 15),
Element(16, "S", "Sulfur", 3, 16),
Element(17, "Cl", "Chlorine", 3, 17),
Element(18, "Ar", "Argon", 3, 18),
Element(19, "K", "Potassium", 4, 1),
Element(20, "Ca", "Calcium", 4, 2),
Element(21, "Sc", "Scandium", 4, 3),
Element(22, "Ti", "Titanium", 4, 4),
Element(23, "V", "Vanadium", 4, 5),
Element(24, "Cr", "Chromium", 4, 6),
Element(25, "Mn", "Manganese", 4, 7),
Element(26, "Fe", "Iron", 4, 8),
Element(27, "Co", "Cobalt", 4, 9),
Element(28, "Ni", "Nickel", 4, 10),
Element(29, "Cu", "Copper", 4, 11),
Element(30, "Zn", "Zinc", 4, 12),
Element(31, "Ga", "Gallium", 4, 13),
Element(32, "Ge", "Germanium", 4, 14),
Element(33, "As", "Arsenic", 4, 15),
Element(34, "Se", "Selenium", 4, 16),
Element(35, "Br", "Bromine", 4, 17),
Element(36, "Kr", "Krypton", 4, 18),
Element(37, "Rb", "Rubidium", 5, 1),
Element(38, "Sr", "Strontium", 5, 2),
Element(39, "Y", "Yttrium", 5, 3),
Element(40, "Zr", "Zirconium", 5, 4),

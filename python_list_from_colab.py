{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled4.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyOKBYgBO1Ngj/xu669LuUs3",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/jayeshmutha221b/learning-python/blob/main/python_list_from_colab.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kc-uBb6PdiNj",
        "outputId": "12f0da8f-5fa1-4489-c1c0-8f62bd045a6d"
      },
      "source": [
        "l1 = ['jayesh','Mutha']\n",
        "l1.append('P')\n",
        "print(l1)\n",
        "\n",
        "#count(element) --> finds count of element in list\n",
        "print('Count of Jayesh in l1 :' ,l1.count('jayesh'))\n",
        "\n",
        "#extend(list) --> Joins two list\n",
        "l2 = ['MS','CS','Python','MS']\n",
        "l1.extend(l2)\n",
        "print(l1)\n",
        "\n",
        "#index(element,start_index,end_index) --> finds index of first occurance of element {start_index,end_index are optional} \n",
        "print('Index of elment MS:',l1.index('MS',3,6))\n",
        "\n",
        "#pop(index) --> removes and returns element at given index , if index not provided returns and removes last element in list\n",
        "print(l1.pop(2))\n",
        "print('element at index 2 poped',l1)\n",
        "\n",
        "#remove(element) --> removes first occurance of element\n",
        "print(l1.remove('MS')) #returns none\n",
        "print('item removed',l1)\n",
        "\n",
        "#reverese \n",
        "l1.reverse()\n",
        "print('reveres',l1)\n",
        "\n",
        "#sort\n",
        "l1.sort()\n",
        "print('sorted list', l1)\n",
        "\n",
        "#clear\n",
        "l1.clear()\n",
        "print('list after clear()', l1)\n"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "['jayesh', 'Mutha', 'P']\n",
            "Count of Jayesh in l1 : 1\n",
            "['jayesh', 'Mutha', 'P', 'MS', 'CS', 'Python', 'MS']\n",
            "Index of elment MS: 3\n",
            "P\n",
            "element at index 2 poped ['jayesh', 'Mutha', 'MS', 'CS', 'Python', 'MS']\n",
            "None\n",
            "item removed ['jayesh', 'Mutha', 'CS', 'Python', 'MS']\n",
            "reveres ['MS', 'Python', 'CS', 'Mutha', 'jayesh']\n",
            "sorted list ['CS', 'MS', 'Mutha', 'Python', 'jayesh']\n",
            "list after clear() []\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}
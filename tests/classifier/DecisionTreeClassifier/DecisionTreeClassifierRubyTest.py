# -*- coding: utf-8 -*-

from unittest import TestCase

from sklearn.tree import DecisionTreeClassifier

from ..Classifier import Classifier
from ...language.Ruby import Ruby


class DecisionTreeClassifierRubyTest(Ruby, Classifier, TestCase):

    def setUp(self):
        super(DecisionTreeClassifierRubyTest, self).setUp()
        self.mdl = DecisionTreeClassifier(random_state=0)

    def tearDown(self):
        super(DecisionTreeClassifierRubyTest, self).tearDown()

#!/usr/bin/python3
""" test cases for user class """
import unittest

class TestUser(unittest.TestCase):
    def test_init(self):
        """ tset initializtaion """
        from models.user import User

        this = User()
        this.first_name = "this"
        this.last_name = "thiston"
        this.email = "this@gmail.com"
        this.password = "12322332"

        dtnary = this.to_dict()
        self.assertEqual(dtnary['first_name'], this.first_name)
        self.assertEqual(dtnary['last_name'], this.last_name)
        self.assertEqual(dtnary['email'], this.email)
        self.assertEqual(dtnary['password'], this.password)

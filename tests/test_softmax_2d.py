import torch
from torch.autograd import Variable
from tests.common import TestCase

from dsntnn import softmax_2d


class TestSoftmax2d(TestCase):
    def test_forward(self):
        in_var = Variable(torch.Tensor([[[10, 1], [5, 2]]]), requires_grad=False)
        expected = torch.Tensor([
            [[0.99285460, 0.00012253],
             [0.00668980, 0.00033307]],
        ])
        actual = softmax_2d(in_var)
        self.assertEqual(actual.data, expected)

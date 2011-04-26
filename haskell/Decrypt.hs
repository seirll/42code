module Decrypt (decrypt) where

import qualified Data.ByteString as B

decrypt :: String -> B.ByteString
decrypt =
	B.pack .
	map (fromIntegral . length . words) .
	lines

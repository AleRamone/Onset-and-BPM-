# Onset-and-BPM-
Python script for obtaining Onset and BPM using Essentia and Librosa libraries. Two guitars play with and without visual information from their partner, so, the differences in onsets and the estimated BPM will be obtained, excluding the silent measures.

The script is essentially a function that scans a folder containing WAV files of guitar recordings playing the same piece. This function compares the Onset and BPM of one guitar with another, also discriminating the trial, condition, and situation in which the guitars were played. Finally, saves in a CSV file for analysis in R while prints the data to the terminal.

Project's abstract

This project continues a line of research with main objectives in the development of a telepresence system to make music over the Internet. Network Musical Performance tools such as [Sagora](https://sagora.org/) offer virtual rehearsal rooms with an audio signal at very low latency. We consider the implementation of visual information in this type of software to be relevant for remote musical performance. We propose to study the effects of visual information on musical performance, by carrying out psychophysical experiments taking into account the BPM and the synchronization of pairs of guitarists playing together and separately. To do this, we set up a workspace, consisting of a recording studio and monitoring room, and we developed scripts to process and analyze data from recordings of couples in different conditions. These experiments yielded results that determined differences between performances with and without visual information.


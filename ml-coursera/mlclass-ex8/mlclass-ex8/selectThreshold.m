function [bestEpsilon bestF1] = selectThreshold(yval, pval)
%SELECTTHRESHOLD Find the best threshold (epsilon) to use for selecting
%outliers
%   [bestEpsilon bestF1] = SELECTTHRESHOLD(yval, pval) finds the best
%   threshold to use for selecting outliers based on the results from a
%   validation set (pval) and the ground truth (yval).
%

bestEpsilon = 0;
bestF1 = 0;
F1 = 0;

yval
pval

stepsize = (max(pval) - min(pval)) / 1000;
for epsilon = min(pval):stepsize:max(pval)
    
    % ====================== YOUR CODE HERE ======================
    % Instructions: Compute the F1 score of choosing epsilon as the
    %               threshold and place the value in F1. The code at the
    %               end of the loop will compare the F1 score for this
    %               choice of epsilon and set it to be the best epsilon if
    %               it is better than the current choice of epsilon.
    %               
    % Note: You can use predictions = (pval < epsilon) to get a binary vector
    %       of 0's and 1's of the outlier predictions


    %This will get a boolean return that convert to binary vector, 0 = false, 1 = true
    %The cvPredictions is a result of boolean that return whether true or false pval is less
    %than epsilon
    cvPredictions = (pval < epsilon);

    %This command is a joint of two vectors that will count each row, if one row valid for two conditioned
    %stated. fp for example, will count how much row that satisfy cvpredictions == 1 && yval == 0
    fp = sum ((cvPredictions == 1) & (yval == 0));
    tp = sum ((cvPredictions == 1) & (yval == 1));
    fn = sum ((cvPredictions == 0) & (yval == 1));


    prec = tp/(tp+fp);
    rec = tp/ (tp + fn);

    F1 = (2*prec*rec)/(prec+rec);


    % =============================================================

    if F1 > bestF1
       bestF1 = F1;
       bestEpsilon = epsilon;
    end
end

end

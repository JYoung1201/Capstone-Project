CREATE TRIGGER trg_UpdateInventory
ON OrderDetails
AFTER INSERT
AS
BEGIN
    DECLARE @ProductID INT, @Quantity INT;
    SELECT @ProductID = i.ProductID, @Quantity = i.Quantity
    FROM inserted i;

    UPDATE Inventory
    SET QuantityInStock = QuantityInStock - @Quantity, LastUpdated = GETDATE()
    WHERE ProductID = @ProductID;
END;
GO
